from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.report_root import ReportRoot
    from .authentication_methods.authentication_methods_request_builder import AuthenticationMethodsRequestBuilder
    from .daily_print_usage_by_printer.daily_print_usage_by_printer_request_builder import DailyPrintUsageByPrinterRequestBuilder
    from .daily_print_usage_by_user.daily_print_usage_by_user_request_builder import DailyPrintUsageByUserRequestBuilder
    from .device_configuration_device_activity.device_configuration_device_activity_request_builder import DeviceConfigurationDeviceActivityRequestBuilder
    from .device_configuration_user_activity.device_configuration_user_activity_request_builder import DeviceConfigurationUserActivityRequestBuilder
    from .get_email_activity_counts_with_period.get_email_activity_counts_with_period_request_builder import GetEmailActivityCountsWithPeriodRequestBuilder
    from .get_email_activity_user_counts_with_period.get_email_activity_user_counts_with_period_request_builder import GetEmailActivityUserCountsWithPeriodRequestBuilder
    from .get_email_activity_user_detail_with_date.get_email_activity_user_detail_with_date_request_builder import GetEmailActivityUserDetailWithDateRequestBuilder
    from .get_email_activity_user_detail_with_period.get_email_activity_user_detail_with_period_request_builder import GetEmailActivityUserDetailWithPeriodRequestBuilder
    from .get_email_app_usage_apps_user_counts_with_period.get_email_app_usage_apps_user_counts_with_period_request_builder import GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder
    from .get_email_app_usage_user_counts_with_period.get_email_app_usage_user_counts_with_period_request_builder import GetEmailAppUsageUserCountsWithPeriodRequestBuilder
    from .get_email_app_usage_user_detail_with_date.get_email_app_usage_user_detail_with_date_request_builder import GetEmailAppUsageUserDetailWithDateRequestBuilder
    from .get_email_app_usage_user_detail_with_period.get_email_app_usage_user_detail_with_period_request_builder import GetEmailAppUsageUserDetailWithPeriodRequestBuilder
    from .get_email_app_usage_versions_user_counts_with_period.get_email_app_usage_versions_user_counts_with_period_request_builder import GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder
    from .get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time.get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder import GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder
    from .get_m365_app_platform_user_counts_with_period.get_m365_app_platform_user_counts_with_period_request_builder import GetM365AppPlatformUserCountsWithPeriodRequestBuilder
    from .get_m365_app_user_counts_with_period.get_m365_app_user_counts_with_period_request_builder import GetM365AppUserCountsWithPeriodRequestBuilder
    from .get_m365_app_user_detail_with_date.get_m365_app_user_detail_with_date_request_builder import GetM365AppUserDetailWithDateRequestBuilder
    from .get_m365_app_user_detail_with_period.get_m365_app_user_detail_with_period_request_builder import GetM365AppUserDetailWithPeriodRequestBuilder
    from .get_mailbox_usage_detail_with_period.get_mailbox_usage_detail_with_period_request_builder import GetMailboxUsageDetailWithPeriodRequestBuilder
    from .get_mailbox_usage_mailbox_counts_with_period.get_mailbox_usage_mailbox_counts_with_period_request_builder import GetMailboxUsageMailboxCountsWithPeriodRequestBuilder
    from .get_mailbox_usage_quota_status_mailbox_counts_with_period.get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder import GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder
    from .get_mailbox_usage_storage_with_period.get_mailbox_usage_storage_with_period_request_builder import GetMailboxUsageStorageWithPeriodRequestBuilder
    from .get_office365_activation_counts.get_office365_activation_counts_request_builder import GetOffice365ActivationCountsRequestBuilder
    from .get_office365_activations_user_counts.get_office365_activations_user_counts_request_builder import GetOffice365ActivationsUserCountsRequestBuilder
    from .get_office365_activations_user_detail.get_office365_activations_user_detail_request_builder import GetOffice365ActivationsUserDetailRequestBuilder
    from .get_office365_active_user_counts_with_period.get_office365_active_user_counts_with_period_request_builder import GetOffice365ActiveUserCountsWithPeriodRequestBuilder
    from .get_office365_active_user_detail_with_date.get_office365_active_user_detail_with_date_request_builder import GetOffice365ActiveUserDetailWithDateRequestBuilder
    from .get_office365_active_user_detail_with_period.get_office365_active_user_detail_with_period_request_builder import GetOffice365ActiveUserDetailWithPeriodRequestBuilder
    from .get_office365_groups_activity_counts_with_period.get_office365_groups_activity_counts_with_period_request_builder import GetOffice365GroupsActivityCountsWithPeriodRequestBuilder
    from .get_office365_groups_activity_detail_with_date.get_office365_groups_activity_detail_with_date_request_builder import GetOffice365GroupsActivityDetailWithDateRequestBuilder
    from .get_office365_groups_activity_detail_with_period.get_office365_groups_activity_detail_with_period_request_builder import GetOffice365GroupsActivityDetailWithPeriodRequestBuilder
    from .get_office365_groups_activity_file_counts_with_period.get_office365_groups_activity_file_counts_with_period_request_builder import GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder
    from .get_office365_groups_activity_group_counts_with_period.get_office365_groups_activity_group_counts_with_period_request_builder import GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder
    from .get_office365_groups_activity_storage_with_period.get_office365_groups_activity_storage_with_period_request_builder import GetOffice365GroupsActivityStorageWithPeriodRequestBuilder
    from .get_office365_services_user_counts_with_period.get_office365_services_user_counts_with_period_request_builder import GetOffice365ServicesUserCountsWithPeriodRequestBuilder
    from .get_one_drive_activity_file_counts_with_period.get_one_drive_activity_file_counts_with_period_request_builder import GetOneDriveActivityFileCountsWithPeriodRequestBuilder
    from .get_one_drive_activity_user_counts_with_period.get_one_drive_activity_user_counts_with_period_request_builder import GetOneDriveActivityUserCountsWithPeriodRequestBuilder
    from .get_one_drive_activity_user_detail_with_date.get_one_drive_activity_user_detail_with_date_request_builder import GetOneDriveActivityUserDetailWithDateRequestBuilder
    from .get_one_drive_activity_user_detail_with_period.get_one_drive_activity_user_detail_with_period_request_builder import GetOneDriveActivityUserDetailWithPeriodRequestBuilder
    from .get_one_drive_usage_account_counts_with_period.get_one_drive_usage_account_counts_with_period_request_builder import GetOneDriveUsageAccountCountsWithPeriodRequestBuilder
    from .get_one_drive_usage_account_detail_with_date.get_one_drive_usage_account_detail_with_date_request_builder import GetOneDriveUsageAccountDetailWithDateRequestBuilder
    from .get_one_drive_usage_account_detail_with_period.get_one_drive_usage_account_detail_with_period_request_builder import GetOneDriveUsageAccountDetailWithPeriodRequestBuilder
    from .get_one_drive_usage_file_counts_with_period.get_one_drive_usage_file_counts_with_period_request_builder import GetOneDriveUsageFileCountsWithPeriodRequestBuilder
    from .get_one_drive_usage_storage_with_period.get_one_drive_usage_storage_with_period_request_builder import GetOneDriveUsageStorageWithPeriodRequestBuilder
    from .get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time.get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder import GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder
    from .get_share_point_activity_file_counts_with_period.get_share_point_activity_file_counts_with_period_request_builder import GetSharePointActivityFileCountsWithPeriodRequestBuilder
    from .get_share_point_activity_pages_with_period.get_share_point_activity_pages_with_period_request_builder import GetSharePointActivityPagesWithPeriodRequestBuilder
    from .get_share_point_activity_user_counts_with_period.get_share_point_activity_user_counts_with_period_request_builder import GetSharePointActivityUserCountsWithPeriodRequestBuilder
    from .get_share_point_activity_user_detail_with_date.get_share_point_activity_user_detail_with_date_request_builder import GetSharePointActivityUserDetailWithDateRequestBuilder
    from .get_share_point_activity_user_detail_with_period.get_share_point_activity_user_detail_with_period_request_builder import GetSharePointActivityUserDetailWithPeriodRequestBuilder
    from .get_share_point_site_usage_detail_with_date.get_share_point_site_usage_detail_with_date_request_builder import GetSharePointSiteUsageDetailWithDateRequestBuilder
    from .get_share_point_site_usage_detail_with_period.get_share_point_site_usage_detail_with_period_request_builder import GetSharePointSiteUsageDetailWithPeriodRequestBuilder
    from .get_share_point_site_usage_file_counts_with_period.get_share_point_site_usage_file_counts_with_period_request_builder import GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder
    from .get_share_point_site_usage_pages_with_period.get_share_point_site_usage_pages_with_period_request_builder import GetSharePointSiteUsagePagesWithPeriodRequestBuilder
    from .get_share_point_site_usage_site_counts_with_period.get_share_point_site_usage_site_counts_with_period_request_builder import GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder
    from .get_share_point_site_usage_storage_with_period.get_share_point_site_usage_storage_with_period_request_builder import GetSharePointSiteUsageStorageWithPeriodRequestBuilder
    from .get_skype_for_business_activity_counts_with_period.get_skype_for_business_activity_counts_with_period_request_builder import GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_activity_user_counts_with_period.get_skype_for_business_activity_user_counts_with_period_request_builder import GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_activity_user_detail_with_date.get_skype_for_business_activity_user_detail_with_date_request_builder import GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder
    from .get_skype_for_business_activity_user_detail_with_period.get_skype_for_business_activity_user_detail_with_period_request_builder import GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder
    from .get_skype_for_business_device_usage_distribution_user_counts_with_period.get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_device_usage_user_counts_with_period.get_skype_for_business_device_usage_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_device_usage_user_detail_with_date.get_skype_for_business_device_usage_user_detail_with_date_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder
    from .get_skype_for_business_device_usage_user_detail_with_period.get_skype_for_business_device_usage_user_detail_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder
    from .get_skype_for_business_organizer_activity_counts_with_period.get_skype_for_business_organizer_activity_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_organizer_activity_minute_counts_with_period.get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder
    from .get_skype_for_business_organizer_activity_user_counts_with_period.get_skype_for_business_organizer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_participant_activity_counts_with_period.get_skype_for_business_participant_activity_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_participant_activity_minute_counts_with_period.get_skype_for_business_participant_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder
    from .get_skype_for_business_participant_activity_user_counts_with_period.get_skype_for_business_participant_activity_user_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder
    from .get_skype_for_business_peer_to_peer_activity_counts_with_period.get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder
    from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period.get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder
    from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period.get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_distribution_user_counts_with_period.get_teams_device_usage_distribution_user_counts_with_period_request_builder import GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_user_counts_with_period.get_teams_device_usage_user_counts_with_period_request_builder import GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder
    from .get_teams_device_usage_user_detail_with_date.get_teams_device_usage_user_detail_with_date_request_builder import GetTeamsDeviceUsageUserDetailWithDateRequestBuilder
    from .get_teams_device_usage_user_detail_with_period.get_teams_device_usage_user_detail_with_period_request_builder import GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder
    from .get_teams_team_activity_counts_with_period.get_teams_team_activity_counts_with_period_request_builder import GetTeamsTeamActivityCountsWithPeriodRequestBuilder
    from .get_teams_team_activity_detail_with_date.get_teams_team_activity_detail_with_date_request_builder import GetTeamsTeamActivityDetailWithDateRequestBuilder
    from .get_teams_team_activity_detail_with_period.get_teams_team_activity_detail_with_period_request_builder import GetTeamsTeamActivityDetailWithPeriodRequestBuilder
    from .get_teams_team_activity_distribution_counts_with_period.get_teams_team_activity_distribution_counts_with_period_request_builder import GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder
    from .get_teams_team_counts_with_period.get_teams_team_counts_with_period_request_builder import GetTeamsTeamCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_counts_with_period.get_teams_user_activity_counts_with_period_request_builder import GetTeamsUserActivityCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_user_counts_with_period.get_teams_user_activity_user_counts_with_period_request_builder import GetTeamsUserActivityUserCountsWithPeriodRequestBuilder
    from .get_teams_user_activity_user_detail_with_date.get_teams_user_activity_user_detail_with_date_request_builder import GetTeamsUserActivityUserDetailWithDateRequestBuilder
    from .get_teams_user_activity_user_detail_with_period.get_teams_user_activity_user_detail_with_period_request_builder import GetTeamsUserActivityUserDetailWithPeriodRequestBuilder
    from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time.get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder import GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder
    from .get_yammer_activity_counts_with_period.get_yammer_activity_counts_with_period_request_builder import GetYammerActivityCountsWithPeriodRequestBuilder
    from .get_yammer_activity_user_counts_with_period.get_yammer_activity_user_counts_with_period_request_builder import GetYammerActivityUserCountsWithPeriodRequestBuilder
    from .get_yammer_activity_user_detail_with_date.get_yammer_activity_user_detail_with_date_request_builder import GetYammerActivityUserDetailWithDateRequestBuilder
    from .get_yammer_activity_user_detail_with_period.get_yammer_activity_user_detail_with_period_request_builder import GetYammerActivityUserDetailWithPeriodRequestBuilder
    from .get_yammer_device_usage_distribution_user_counts_with_period.get_yammer_device_usage_distribution_user_counts_with_period_request_builder import GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
    from .get_yammer_device_usage_user_counts_with_period.get_yammer_device_usage_user_counts_with_period_request_builder import GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder
    from .get_yammer_device_usage_user_detail_with_date.get_yammer_device_usage_user_detail_with_date_request_builder import GetYammerDeviceUsageUserDetailWithDateRequestBuilder
    from .get_yammer_device_usage_user_detail_with_period.get_yammer_device_usage_user_detail_with_period_request_builder import GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder
    from .get_yammer_groups_activity_counts_with_period.get_yammer_groups_activity_counts_with_period_request_builder import GetYammerGroupsActivityCountsWithPeriodRequestBuilder
    from .get_yammer_groups_activity_detail_with_date.get_yammer_groups_activity_detail_with_date_request_builder import GetYammerGroupsActivityDetailWithDateRequestBuilder
    from .get_yammer_groups_activity_detail_with_period.get_yammer_groups_activity_detail_with_period_request_builder import GetYammerGroupsActivityDetailWithPeriodRequestBuilder
    from .get_yammer_groups_activity_group_counts_with_period.get_yammer_groups_activity_group_counts_with_period_request_builder import GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder
    from .managed_device_enrollment_failure_details.managed_device_enrollment_failure_details_request_builder import ManagedDeviceEnrollmentFailureDetailsRequestBuilder
    from .managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
    from .managed_device_enrollment_top_failures.managed_device_enrollment_top_failures_request_builder import ManagedDeviceEnrollmentTopFailuresRequestBuilder
    from .managed_device_enrollment_top_failures_with_period.managed_device_enrollment_top_failures_with_period_request_builder import ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder
    from .monthly_print_usage_by_printer.monthly_print_usage_by_printer_request_builder import MonthlyPrintUsageByPrinterRequestBuilder
    from .monthly_print_usage_by_user.monthly_print_usage_by_user_request_builder import MonthlyPrintUsageByUserRequestBuilder
    from .security.security_request_builder import SecurityRequestBuilder

class ReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reportRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/reports{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[ReportRoot]:
        """
        Read properties and relationships of the reportRoot object.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ReportRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.report_root import ReportRoot

        return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)
    
    def get_email_activity_counts_with_period(self,period: Optional[str] = None) -> GetEmailActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetEmailActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_activity_counts_with_period.get_email_activity_counts_with_period_request_builder import GetEmailActivityCountsWithPeriodRequestBuilder

        return GetEmailActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetEmailActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_activity_user_counts_with_period.get_email_activity_user_counts_with_period_request_builder import GetEmailActivityUserCountsWithPeriodRequestBuilder

        return GetEmailActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetEmailActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetEmailActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_email_activity_user_detail_with_date.get_email_activity_user_detail_with_date_request_builder import GetEmailActivityUserDetailWithDateRequestBuilder

        return GetEmailActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_email_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetEmailActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetEmailActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_activity_user_detail_with_period.get_email_activity_user_detail_with_period_request_builder import GetEmailActivityUserDetailWithPeriodRequestBuilder

        return GetEmailActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_apps_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageAppsUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_apps_user_counts_with_period.get_email_app_usage_apps_user_counts_with_period_request_builder import GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder

        return GetEmailAppUsageAppsUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetEmailAppUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_user_counts_with_period.get_email_app_usage_user_counts_with_period_request_builder import GetEmailAppUsageUserCountsWithPeriodRequestBuilder

        return GetEmailAppUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetEmailAppUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetEmailAppUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_email_app_usage_user_detail_with_date.get_email_app_usage_user_detail_with_date_request_builder import GetEmailAppUsageUserDetailWithDateRequestBuilder

        return GetEmailAppUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_email_app_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetEmailAppUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_user_detail_with_period.get_email_app_usage_user_detail_with_period_request_builder import GetEmailAppUsageUserDetailWithPeriodRequestBuilder

        return GetEmailAppUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_email_app_usage_versions_user_counts_with_period(self,period: Optional[str] = None) -> GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getEmailAppUsageVersionsUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_email_app_usage_versions_user_counts_with_period.get_email_app_usage_versions_user_counts_with_period_request_builder import GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder

        return GetEmailAppUsageVersionsUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime.datetime] = None, group_id: Optional[str] = None, start_date_time: Optional[datetime.datetime] = None) -> GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getGroupArchivedPrintJobs method.
        Args:
            end_date_time: Usage: endDateTime={endDateTime}
            group_id: Usage: groupId='{groupId}'
            start_date_time: Usage: startDateTime={startDateTime}
        Returns: GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not group_id:
            raise TypeError("group_id cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time.get_group_archived_print_jobs_with_group_id_with_start_date_time_with_end_date_time_request_builder import GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder

        return GetGroupArchivedPrintJobsWithGroupIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, group_id, start_date_time)
    
    def get_m365_app_platform_user_counts_with_period(self,period: Optional[str] = None) -> GetM365AppPlatformUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppPlatformUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetM365AppPlatformUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_m365_app_platform_user_counts_with_period.get_m365_app_platform_user_counts_with_period_request_builder import GetM365AppPlatformUserCountsWithPeriodRequestBuilder

        return GetM365AppPlatformUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_m365_app_user_counts_with_period(self,period: Optional[str] = None) -> GetM365AppUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetM365AppUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_m365_app_user_counts_with_period.get_m365_app_user_counts_with_period_request_builder import GetM365AppUserCountsWithPeriodRequestBuilder

        return GetM365AppUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_m365_app_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetM365AppUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getM365AppUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetM365AppUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_m365_app_user_detail_with_date.get_m365_app_user_detail_with_date_request_builder import GetM365AppUserDetailWithDateRequestBuilder

        return GetM365AppUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_m365_app_user_detail_with_period(self,period: Optional[str] = None) -> GetM365AppUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getM365AppUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetM365AppUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_m365_app_user_detail_with_period.get_m365_app_user_detail_with_period_request_builder import GetM365AppUserDetailWithPeriodRequestBuilder

        return GetM365AppUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_detail_with_period(self,period: Optional[str] = None) -> GetMailboxUsageDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetMailboxUsageDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_detail_with_period.get_mailbox_usage_detail_with_period_request_builder import GetMailboxUsageDetailWithPeriodRequestBuilder

        return GetMailboxUsageDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_mailbox_counts_with_period(self,period: Optional[str] = None) -> GetMailboxUsageMailboxCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageMailboxCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetMailboxUsageMailboxCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_mailbox_counts_with_period.get_mailbox_usage_mailbox_counts_with_period_request_builder import GetMailboxUsageMailboxCountsWithPeriodRequestBuilder

        return GetMailboxUsageMailboxCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_quota_status_mailbox_counts_with_period(self,period: Optional[str] = None) -> GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageQuotaStatusMailboxCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_quota_status_mailbox_counts_with_period.get_mailbox_usage_quota_status_mailbox_counts_with_period_request_builder import GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder

        return GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_mailbox_usage_storage_with_period(self,period: Optional[str] = None) -> GetMailboxUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getMailboxUsageStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: GetMailboxUsageStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_mailbox_usage_storage_with_period.get_mailbox_usage_storage_with_period_request_builder import GetMailboxUsageStorageWithPeriodRequestBuilder

        return GetMailboxUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_active_user_counts_with_period(self,period: Optional[str] = None) -> GetOffice365ActiveUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365ActiveUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_active_user_counts_with_period.get_office365_active_user_counts_with_period_request_builder import GetOffice365ActiveUserCountsWithPeriodRequestBuilder

        return GetOffice365ActiveUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_active_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOffice365ActiveUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetOffice365ActiveUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_office365_active_user_detail_with_date.get_office365_active_user_detail_with_date_request_builder import GetOffice365ActiveUserDetailWithDateRequestBuilder

        return GetOffice365ActiveUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_office365_active_user_detail_with_period(self,period: Optional[str] = None) -> GetOffice365ActiveUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ActiveUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365ActiveUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_active_user_detail_with_period.get_office365_active_user_detail_with_period_request_builder import GetOffice365ActiveUserDetailWithPeriodRequestBuilder

        return GetOffice365ActiveUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_counts_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_counts_with_period.get_office365_groups_activity_counts_with_period_request_builder import GetOffice365GroupsActivityCountsWithPeriodRequestBuilder

        return GetOffice365GroupsActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOffice365GroupsActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetOffice365GroupsActivityDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_office365_groups_activity_detail_with_date.get_office365_groups_activity_detail_with_date_request_builder import GetOffice365GroupsActivityDetailWithDateRequestBuilder

        return GetOffice365GroupsActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_office365_groups_activity_detail_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_detail_with_period.get_office365_groups_activity_detail_with_period_request_builder import GetOffice365GroupsActivityDetailWithPeriodRequestBuilder

        return GetOffice365GroupsActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_file_counts_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_file_counts_with_period.get_office365_groups_activity_file_counts_with_period_request_builder import GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder

        return GetOffice365GroupsActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_group_counts_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityGroupCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_group_counts_with_period.get_office365_groups_activity_group_counts_with_period_request_builder import GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder

        return GetOffice365GroupsActivityGroupCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_groups_activity_storage_with_period(self,period: Optional[str] = None) -> GetOffice365GroupsActivityStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365GroupsActivityStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365GroupsActivityStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_groups_activity_storage_with_period.get_office365_groups_activity_storage_with_period_request_builder import GetOffice365GroupsActivityStorageWithPeriodRequestBuilder

        return GetOffice365GroupsActivityStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_office365_services_user_counts_with_period(self,period: Optional[str] = None) -> GetOffice365ServicesUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOffice365ServicesUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOffice365ServicesUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_office365_services_user_counts_with_period.get_office365_services_user_counts_with_period_request_builder import GetOffice365ServicesUserCountsWithPeriodRequestBuilder

        return GetOffice365ServicesUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_file_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOneDriveActivityFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_activity_file_counts_with_period.get_one_drive_activity_file_counts_with_period_request_builder import GetOneDriveActivityFileCountsWithPeriodRequestBuilder

        return GetOneDriveActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOneDriveActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_activity_user_counts_with_period.get_one_drive_activity_user_counts_with_period_request_builder import GetOneDriveActivityUserCountsWithPeriodRequestBuilder

        return GetOneDriveActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOneDriveActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetOneDriveActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_one_drive_activity_user_detail_with_date.get_one_drive_activity_user_detail_with_date_request_builder import GetOneDriveActivityUserDetailWithDateRequestBuilder

        return GetOneDriveActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_one_drive_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetOneDriveActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOneDriveActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_activity_user_detail_with_period.get_one_drive_activity_user_detail_with_period_request_builder import GetOneDriveActivityUserDetailWithPeriodRequestBuilder

        return GetOneDriveActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_account_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageAccountCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOneDriveUsageAccountCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_account_counts_with_period.get_one_drive_usage_account_counts_with_period_request_builder import GetOneDriveUsageAccountCountsWithPeriodRequestBuilder

        return GetOneDriveUsageAccountCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_account_detail_with_date(self,date: Optional[datetime.date] = None) -> GetOneDriveUsageAccountDetailWithDateRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetOneDriveUsageAccountDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_one_drive_usage_account_detail_with_date.get_one_drive_usage_account_detail_with_date_request_builder import GetOneDriveUsageAccountDetailWithDateRequestBuilder

        return GetOneDriveUsageAccountDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_one_drive_usage_account_detail_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageAccountDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageAccountDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOneDriveUsageAccountDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_account_detail_with_period.get_one_drive_usage_account_detail_with_period_request_builder import GetOneDriveUsageAccountDetailWithPeriodRequestBuilder

        return GetOneDriveUsageAccountDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_file_counts_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOneDriveUsageFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_file_counts_with_period.get_one_drive_usage_file_counts_with_period_request_builder import GetOneDriveUsageFileCountsWithPeriodRequestBuilder

        return GetOneDriveUsageFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_one_drive_usage_storage_with_period(self,period: Optional[str] = None) -> GetOneDriveUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getOneDriveUsageStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: GetOneDriveUsageStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_one_drive_usage_storage_with_period.get_one_drive_usage_storage_with_period_request_builder import GetOneDriveUsageStorageWithPeriodRequestBuilder

        return GetOneDriveUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime.datetime] = None, printer_id: Optional[str] = None, start_date_time: Optional[datetime.datetime] = None) -> GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getPrinterArchivedPrintJobs method.
        Args:
            end_date_time: Usage: endDateTime={endDateTime}
            printer_id: Usage: printerId='{printerId}'
            start_date_time: Usage: startDateTime={startDateTime}
        Returns: GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not printer_id:
            raise TypeError("printer_id cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        from .get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time.get_printer_archived_print_jobs_with_printer_id_with_start_date_time_with_end_date_time_request_builder import GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder

        return GetPrinterArchivedPrintJobsWithPrinterIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, printer_id, start_date_time)
    
    def get_share_point_activity_file_counts_with_period(self,period: Optional[str] = None) -> GetSharePointActivityFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointActivityFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_file_counts_with_period.get_share_point_activity_file_counts_with_period_request_builder import GetSharePointActivityFileCountsWithPeriodRequestBuilder

        return GetSharePointActivityFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_pages_with_period(self,period: Optional[str] = None) -> GetSharePointActivityPagesWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityPages method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointActivityPagesWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_pages_with_period.get_share_point_activity_pages_with_period_request_builder import GetSharePointActivityPagesWithPeriodRequestBuilder

        return GetSharePointActivityPagesWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSharePointActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_user_counts_with_period.get_share_point_activity_user_counts_with_period_request_builder import GetSharePointActivityUserCountsWithPeriodRequestBuilder

        return GetSharePointActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSharePointActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetSharePointActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_share_point_activity_user_detail_with_date.get_share_point_activity_user_detail_with_date_request_builder import GetSharePointActivityUserDetailWithDateRequestBuilder

        return GetSharePointActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_share_point_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetSharePointActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_activity_user_detail_with_period.get_share_point_activity_user_detail_with_period_request_builder import GetSharePointActivityUserDetailWithPeriodRequestBuilder

        return GetSharePointActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSharePointSiteUsageDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetSharePointSiteUsageDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_share_point_site_usage_detail_with_date.get_share_point_site_usage_detail_with_date_request_builder import GetSharePointSiteUsageDetailWithDateRequestBuilder

        return GetSharePointSiteUsageDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_share_point_site_usage_detail_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_detail_with_period.get_share_point_site_usage_detail_with_period_request_builder import GetSharePointSiteUsageDetailWithPeriodRequestBuilder

        return GetSharePointSiteUsageDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_file_counts_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageFileCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_file_counts_with_period.get_share_point_site_usage_file_counts_with_period_request_builder import GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder

        return GetSharePointSiteUsageFileCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_pages_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsagePagesWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsagePages method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointSiteUsagePagesWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_pages_with_period.get_share_point_site_usage_pages_with_period_request_builder import GetSharePointSiteUsagePagesWithPeriodRequestBuilder

        return GetSharePointSiteUsagePagesWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_site_counts_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageSiteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_site_counts_with_period.get_share_point_site_usage_site_counts_with_period_request_builder import GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder

        return GetSharePointSiteUsageSiteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_share_point_site_usage_storage_with_period(self,period: Optional[str] = None) -> GetSharePointSiteUsageStorageWithPeriodRequestBuilder:
        """
        Provides operations to call the getSharePointSiteUsageStorage method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSharePointSiteUsageStorageWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_share_point_site_usage_storage_with_period.get_share_point_site_usage_storage_with_period_request_builder import GetSharePointSiteUsageStorageWithPeriodRequestBuilder

        return GetSharePointSiteUsageStorageWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_activity_counts_with_period.get_skype_for_business_activity_counts_with_period_request_builder import GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_activity_user_counts_with_period.get_skype_for_business_activity_user_counts_with_period_request_builder import GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_skype_for_business_activity_user_detail_with_date.get_skype_for_business_activity_user_detail_with_date_request_builder import GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder

        return GetSkypeForBusinessActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_skype_for_business_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_activity_user_detail_with_period.get_skype_for_business_activity_user_detail_with_period_request_builder import GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder

        return GetSkypeForBusinessActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_device_usage_distribution_user_counts_with_period.get_skype_for_business_device_usage_distribution_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_device_usage_user_counts_with_period.get_skype_for_business_device_usage_user_counts_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_device_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_skype_for_business_device_usage_user_detail_with_date.get_skype_for_business_device_usage_user_detail_with_date_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder

        return GetSkypeForBusinessDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_skype_for_business_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessDeviceUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_device_usage_user_detail_with_period.get_skype_for_business_device_usage_user_detail_with_period_request_builder import GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder

        return GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_organizer_activity_counts_with_period.get_skype_for_business_organizer_activity_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_minute_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityMinuteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_organizer_activity_minute_counts_with_period.get_skype_for_business_organizer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_organizer_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessOrganizerActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_organizer_activity_user_counts_with_period.get_skype_for_business_organizer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_participant_activity_counts_with_period.get_skype_for_business_participant_activity_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessParticipantActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_minute_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityMinuteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_participant_activity_minute_counts_with_period.get_skype_for_business_participant_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_participant_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessParticipantActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_participant_activity_user_counts_with_period.get_skype_for_business_participant_activity_user_counts_with_period_request_builder import GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_peer_to_peer_activity_counts_with_period.get_skype_for_business_peer_to_peer_activity_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_minute_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityMinuteCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period.get_skype_for_business_peer_to_peer_activity_minute_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_skype_for_business_peer_to_peer_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getSkypeForBusinessPeerToPeerActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period.get_skype_for_business_peer_to_peer_activity_user_counts_with_period_request_builder import GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder

        return GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_distribution_user_counts_with_period.get_teams_device_usage_distribution_user_counts_with_period_request_builder import GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder

        return GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_user_counts_with_period.get_teams_device_usage_user_counts_with_period_request_builder import GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder

        return GetTeamsDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_device_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetTeamsDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetTeamsDeviceUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_teams_device_usage_user_detail_with_date.get_teams_device_usage_user_detail_with_date_request_builder import GetTeamsDeviceUsageUserDetailWithDateRequestBuilder

        return GetTeamsDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsDeviceUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_device_usage_user_detail_with_period.get_teams_device_usage_user_detail_with_period_request_builder import GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder

        return GetTeamsDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_counts_with_period(self,period: Optional[str] = None) -> GetTeamsTeamActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsTeamActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_activity_counts_with_period.get_teams_team_activity_counts_with_period_request_builder import GetTeamsTeamActivityCountsWithPeriodRequestBuilder

        return GetTeamsTeamActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_detail_with_date(self,date: Optional[datetime.date] = None) -> GetTeamsTeamActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetTeamsTeamActivityDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_teams_team_activity_detail_with_date.get_teams_team_activity_detail_with_date_request_builder import GetTeamsTeamActivityDetailWithDateRequestBuilder

        return GetTeamsTeamActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_team_activity_detail_with_period(self,period: Optional[str] = None) -> GetTeamsTeamActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsTeamActivityDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_activity_detail_with_period.get_teams_team_activity_detail_with_period_request_builder import GetTeamsTeamActivityDetailWithPeriodRequestBuilder

        return GetTeamsTeamActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_activity_distribution_counts_with_period(self,period: Optional[str] = None) -> GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamActivityDistributionCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_activity_distribution_counts_with_period.get_teams_team_activity_distribution_counts_with_period_request_builder import GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder

        return GetTeamsTeamActivityDistributionCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_team_counts_with_period(self,period: Optional[str] = None) -> GetTeamsTeamCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsTeamCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsTeamCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_team_counts_with_period.get_teams_team_counts_with_period_request_builder import GetTeamsTeamCountsWithPeriodRequestBuilder

        return GetTeamsTeamCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsUserActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_counts_with_period.get_teams_user_activity_counts_with_period_request_builder import GetTeamsUserActivityCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsUserActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_user_counts_with_period.get_teams_user_activity_user_counts_with_period_request_builder import GetTeamsUserActivityUserCountsWithPeriodRequestBuilder

        return GetTeamsUserActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_teams_user_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetTeamsUserActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetTeamsUserActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_teams_user_activity_user_detail_with_date.get_teams_user_activity_user_detail_with_date_request_builder import GetTeamsUserActivityUserDetailWithDateRequestBuilder

        return GetTeamsUserActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_teams_user_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetTeamsUserActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getTeamsUserActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetTeamsUserActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_teams_user_activity_user_detail_with_period.get_teams_user_activity_user_detail_with_period_request_builder import GetTeamsUserActivityUserDetailWithPeriodRequestBuilder

        return GetTeamsUserActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time(self,end_date_time: Optional[datetime.datetime] = None, start_date_time: Optional[datetime.datetime] = None, user_id: Optional[str] = None) -> GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the getUserArchivedPrintJobs method.
        Args:
            end_date_time: Usage: endDateTime={endDateTime}
            start_date_time: Usage: startDateTime={startDateTime}
            user_id: Usage: userId='{userId}'
        Returns: GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if not end_date_time:
            raise TypeError("end_date_time cannot be null.")
        if not start_date_time:
            raise TypeError("start_date_time cannot be null.")
        if not user_id:
            raise TypeError("user_id cannot be null.")
        from .get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time.get_user_archived_print_jobs_with_user_id_with_start_date_time_with_end_date_time_request_builder import GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder

        return GetUserArchivedPrintJobsWithUserIdWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time, user_id)
    
    def get_yammer_activity_counts_with_period(self,period: Optional[str] = None) -> GetYammerActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_activity_counts_with_period.get_yammer_activity_counts_with_period_request_builder import GetYammerActivityCountsWithPeriodRequestBuilder

        return GetYammerActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_activity_user_counts_with_period(self,period: Optional[str] = None) -> GetYammerActivityUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerActivityUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_activity_user_counts_with_period.get_yammer_activity_user_counts_with_period_request_builder import GetYammerActivityUserCountsWithPeriodRequestBuilder

        return GetYammerActivityUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_activity_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetYammerActivityUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetYammerActivityUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_yammer_activity_user_detail_with_date.get_yammer_activity_user_detail_with_date_request_builder import GetYammerActivityUserDetailWithDateRequestBuilder

        return GetYammerActivityUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_activity_user_detail_with_period(self,period: Optional[str] = None) -> GetYammerActivityUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerActivityUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerActivityUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_activity_user_detail_with_period.get_yammer_activity_user_detail_with_period_request_builder import GetYammerActivityUserDetailWithPeriodRequestBuilder

        return GetYammerActivityUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_distribution_user_counts_with_period(self,period: Optional[str] = None) -> GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageDistributionUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_device_usage_distribution_user_counts_with_period.get_yammer_device_usage_distribution_user_counts_with_period_request_builder import GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder

        return GetYammerDeviceUsageDistributionUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_user_counts_with_period(self,period: Optional[str] = None) -> GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_device_usage_user_counts_with_period.get_yammer_device_usage_user_counts_with_period_request_builder import GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder

        return GetYammerDeviceUsageUserCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_device_usage_user_detail_with_date(self,date: Optional[datetime.date] = None) -> GetYammerDeviceUsageUserDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetYammerDeviceUsageUserDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_yammer_device_usage_user_detail_with_date.get_yammer_device_usage_user_detail_with_date_request_builder import GetYammerDeviceUsageUserDetailWithDateRequestBuilder

        return GetYammerDeviceUsageUserDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_device_usage_user_detail_with_period(self,period: Optional[str] = None) -> GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerDeviceUsageUserDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_device_usage_user_detail_with_period.get_yammer_device_usage_user_detail_with_period_request_builder import GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder

        return GetYammerDeviceUsageUserDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_counts_with_period(self,period: Optional[str] = None) -> GetYammerGroupsActivityCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerGroupsActivityCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_groups_activity_counts_with_period.get_yammer_groups_activity_counts_with_period_request_builder import GetYammerGroupsActivityCountsWithPeriodRequestBuilder

        return GetYammerGroupsActivityCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_detail_with_date(self,date: Optional[datetime.date] = None) -> GetYammerGroupsActivityDetailWithDateRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityDetail method.
        Args:
            date: Usage: date={date}
        Returns: GetYammerGroupsActivityDetailWithDateRequestBuilder
        """
        if not date:
            raise TypeError("date cannot be null.")
        from .get_yammer_groups_activity_detail_with_date.get_yammer_groups_activity_detail_with_date_request_builder import GetYammerGroupsActivityDetailWithDateRequestBuilder

        return GetYammerGroupsActivityDetailWithDateRequestBuilder(self.request_adapter, self.path_parameters, date)
    
    def get_yammer_groups_activity_detail_with_period(self,period: Optional[str] = None) -> GetYammerGroupsActivityDetailWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityDetail method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerGroupsActivityDetailWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_groups_activity_detail_with_period.get_yammer_groups_activity_detail_with_period_request_builder import GetYammerGroupsActivityDetailWithPeriodRequestBuilder

        return GetYammerGroupsActivityDetailWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def get_yammer_groups_activity_group_counts_with_period(self,period: Optional[str] = None) -> GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder:
        """
        Provides operations to call the getYammerGroupsActivityGroupCounts method.
        Args:
            period: Usage: period='{period}'
        Returns: GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .get_yammer_groups_activity_group_counts_with_period.get_yammer_groups_activity_group_counts_with_period_request_builder import GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder

        return GetYammerGroupsActivityGroupCountsWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    def managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token(self,filter: Optional[str] = None, skip: Optional[int] = None, skip_token: Optional[str] = None, top: Optional[int] = None) -> ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureDetails method.
        Args:
            filter: Usage: filter='{filter}'
            skip: Usage: skip={skip}
            skip_token: Usage: skipToken='{skipToken}'
            top: Usage: top={top}
        Returns: ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder
        """
        if not filter:
            raise TypeError("filter cannot be null.")
        if not skip:
            raise TypeError("skip cannot be null.")
        if not skip_token:
            raise TypeError("skip_token cannot be null.")
        if not top:
            raise TypeError("top cannot be null.")
        from .managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token.managed_device_enrollment_failure_details_with_skip_with_top_with_filter_with_skip_token_request_builder import ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder

        return ManagedDeviceEnrollmentFailureDetailsWithSkipWithTopWithFilterWithSkipTokenRequestBuilder(self.request_adapter, self.path_parameters, filter, skip, skip_token, top)
    
    def managed_device_enrollment_top_failures_with_period(self,period: Optional[str] = None) -> ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentTopFailures method.
        Args:
            period: Usage: period='{period}'
        Returns: ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder
        """
        if not period:
            raise TypeError("period cannot be null.")
        from .managed_device_enrollment_top_failures_with_period.managed_device_enrollment_top_failures_with_period_request_builder import ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder

        return ManagedDeviceEnrollmentTopFailuresWithPeriodRequestBuilder(self.request_adapter, self.path_parameters, period)
    
    async def patch(self,body: Optional[ReportRoot] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> Optional[ReportRoot]:
        """
        Update the properties of a reportRoot object.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ReportRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.report_root import ReportRoot

        return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read properties and relationships of the reportRoot object.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[ReportRoot] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a reportRoot object.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def authentication_methods(self) -> AuthenticationMethodsRequestBuilder:
        """
        Provides operations to manage the authenticationMethods property of the microsoft.graph.reportRoot entity.
        """
        from .authentication_methods.authentication_methods_request_builder import AuthenticationMethodsRequestBuilder

        return AuthenticationMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_by_printer(self) -> DailyPrintUsageByPrinterRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_by_printer.daily_print_usage_by_printer_request_builder import DailyPrintUsageByPrinterRequestBuilder

        return DailyPrintUsageByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def daily_print_usage_by_user(self) -> DailyPrintUsageByUserRequestBuilder:
        """
        Provides operations to manage the dailyPrintUsageByUser property of the microsoft.graph.reportRoot entity.
        """
        from .daily_print_usage_by_user.daily_print_usage_by_user_request_builder import DailyPrintUsageByUserRequestBuilder

        return DailyPrintUsageByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_device_activity(self) -> DeviceConfigurationDeviceActivityRequestBuilder:
        """
        Provides operations to call the deviceConfigurationDeviceActivity method.
        """
        from .device_configuration_device_activity.device_configuration_device_activity_request_builder import DeviceConfigurationDeviceActivityRequestBuilder

        return DeviceConfigurationDeviceActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_user_activity(self) -> DeviceConfigurationUserActivityRequestBuilder:
        """
        Provides operations to call the deviceConfigurationUserActivity method.
        """
        from .device_configuration_user_activity.device_configuration_user_activity_request_builder import DeviceConfigurationUserActivityRequestBuilder

        return DeviceConfigurationUserActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activation_counts(self) -> GetOffice365ActivationCountsRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationCounts method.
        """
        from .get_office365_activation_counts.get_office365_activation_counts_request_builder import GetOffice365ActivationCountsRequestBuilder

        return GetOffice365ActivationCountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activations_user_counts(self) -> GetOffice365ActivationsUserCountsRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationsUserCounts method.
        """
        from .get_office365_activations_user_counts.get_office365_activations_user_counts_request_builder import GetOffice365ActivationsUserCountsRequestBuilder

        return GetOffice365ActivationsUserCountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_office365_activations_user_detail(self) -> GetOffice365ActivationsUserDetailRequestBuilder:
        """
        Provides operations to call the getOffice365ActivationsUserDetail method.
        """
        from .get_office365_activations_user_detail.get_office365_activations_user_detail_request_builder import GetOffice365ActivationsUserDetailRequestBuilder

        return GetOffice365ActivationsUserDetailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_failure_details(self) -> ManagedDeviceEnrollmentFailureDetailsRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentFailureDetails method.
        """
        from .managed_device_enrollment_failure_details.managed_device_enrollment_failure_details_request_builder import ManagedDeviceEnrollmentFailureDetailsRequestBuilder

        return ManagedDeviceEnrollmentFailureDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_enrollment_top_failures(self) -> ManagedDeviceEnrollmentTopFailuresRequestBuilder:
        """
        Provides operations to call the managedDeviceEnrollmentTopFailures method.
        """
        from .managed_device_enrollment_top_failures.managed_device_enrollment_top_failures_request_builder import ManagedDeviceEnrollmentTopFailuresRequestBuilder

        return ManagedDeviceEnrollmentTopFailuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_by_printer(self) -> MonthlyPrintUsageByPrinterRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageByPrinter property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_by_printer.monthly_print_usage_by_printer_request_builder import MonthlyPrintUsageByPrinterRequestBuilder

        return MonthlyPrintUsageByPrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def monthly_print_usage_by_user(self) -> MonthlyPrintUsageByUserRequestBuilder:
        """
        Provides operations to manage the monthlyPrintUsageByUser property of the microsoft.graph.reportRoot entity.
        """
        from .monthly_print_usage_by_user.monthly_print_usage_by_user_request_builder import MonthlyPrintUsageByUserRequestBuilder

        return MonthlyPrintUsageByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> SecurityRequestBuilder:
        """
        Provides operations to manage the security property of the microsoft.graph.reportRoot entity.
        """
        from .security.security_request_builder import SecurityRequestBuilder

        return SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the reportRoot object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ReportsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ReportsRequestBuilder.ReportsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

